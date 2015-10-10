#[macro_use]
extern crate lazy_static;
extern crate capnp;
extern crate capnp_rpc;
extern crate cassandra;

use std::collections::HashMap;
use capnp::capability::{Server};
use capnp_rpc::ez_rpc::EzRpcServer;
use cassandra::*;

pub mod killranswers_capnp {
  include!(concat!(env!("OUT_DIR"), "/killranswers_capnp.rs"));
}

static CREATE_USER : &'static str = "insert into user (user_id), values (?)";

lazy_static! {

}

use killranswers_capnp::killr_answers;

struct KillrAnswersImpl;

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
    let ka = Box::new(killr_answers::ServerDispatch { server : Box::new(KillrAnswersImpl)});
    //
    rpc_server.serve(ka);

    println!("Done");
}
