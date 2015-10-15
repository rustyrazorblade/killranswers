#[macro_use]
extern crate capnp;
extern crate capnp_rpc;
extern crate cassandra;

use std::collections::HashMap;
use capnp::capability::{Server};
use capnp_rpc::ez_rpc::EzRpcServer;
use cassandra::*;

// this is generated automatically as part of the build process
// see build.rs
pub mod killranswers_capnp {
  include!(concat!(env!("OUT_DIR"), "/killranswers_capnp.rs"));
}
use killranswers_capnp::killr_answers;

// queries for prepared statements
// schema is managed in the python part of the app
// see the cqlengine Models
static CREATE_USER : &'static str = "insert into killranswers.user (user_id) values (?)";


struct KillrAnswersImpl {
    db: Session,
    queries: HashMap<String, PreparedStatement>,
}

impl KillrAnswersImpl {
    // returns a Boxed implemention
    fn new() -> Result<Box<KillrAnswersImpl>, CassandraError> {

        let mut cluster = Cluster::new();
        println!("Cluster created");
        cluster.set_contact_points("127.0.0.1").unwrap();
        println!("Setting protocol version");
        // cluster.set_protocol_version(3).unwrap();
        println!("connecting");
        let mut session = cluster.connect().unwrap();
        println!("Connected");
        // closure to prepare statement
        let mut queries = HashMap::new();

        println!("preparing");
        let mut prepared = try!(session.prepare(CREATE_USER));
        //
        println!("unwrapping and waiting");
        match prepared.wait() {
            Ok(prepared) => {
                let name = "CREATE_USER".to_string();
                queries.insert(name, prepared);
            }
            Err(err) => {
                println!("BAD NEWS FAIL");
                panic!(err);
            }
        }
        println!("new() done");
        Ok(Box::new(KillrAnswersImpl{ db: session, queries: queries }))
    }
}

impl killr_answers::Server for KillrAnswersImpl {
    // fn ask(&mut self, mut context: killr_answers::AskContext) {
    //     println!("Asking");
    // }
    fn register_user(&mut self, mut context: killr_answers::RegisterUserContext) {
        context.done();
    }

}

fn main() {
    println!("Starting up...");

    let rpc_server = EzRpcServer::new("127.0.0.1:6000").unwrap();
    let server = KillrAnswersImpl::new().unwrap();
    let ka = Box::new(killr_answers::ServerDispatch { server : server });
    //
    rpc_server.serve(ka);

    println!("Done");
}
