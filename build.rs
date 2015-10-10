extern crate capnpc;

fn main() {
    ::capnpc::compile(".", &["killranswers.capnp"]).unwrap();
}
