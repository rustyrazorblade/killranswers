extern crate capnp;
extern crate capnp_rpc;
// extern crate killranswers_capnp;

use capnp::capability::{Server};
use capnp_rpc::ez_rpc::EzRpcServer;
// use killranswers_capnp::killranswers;


fn main() {
    println!("Starting up...");
    let rpc_server = EzRpcServer::new("6000").unwrap();
    // let killranswers = Box::new(calculator::ServerDispatch { server : Box::new(CalculatorImpl)});
    //
    // rpc_server.serve(killranswers);

    println!("Done");
}
