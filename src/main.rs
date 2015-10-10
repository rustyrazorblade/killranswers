extern crate capnp;
extern crate capnp_rpc;
// extern crate killranswers_capnp;

use capnp::capability::{Server};
use capnp_rpc::ez_rpc::EzRpcServer;
// use killranswers_capnp::killranswers;

pub mod killranswers_capnp {
  include!(concat!(env!("OUT_DIR"), "/killranswers_capnp.rs"));
}

use killranswers_capnp::killr_answers;

struct KillrAnswersImpl;

impl killr_answers::Server for KillrAnswersImpl {
    fn ask(&mut self, mut context: killr_answers::AskContext) {

    }
    fn register_user(&mut self, mut context: killr_answers::RegisterUserContext) {
        
    }

}

fn main() {
    println!("Starting up...");
    let rpc_server = EzRpcServer::new("localhost:6000").unwrap();
    let ka = Box::new(killr_answers::ServerDispatch { server : Box::new(KillrAnswersImpl)});
    //
    rpc_server.serve(ka);

    println!("Done");
}
