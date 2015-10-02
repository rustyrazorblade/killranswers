@0xce4c7cd66480f6f2;

interface KillrAnswers {
    ask @0 (text :Text, category :Text, user :Text) -> (question: Text);
    createCategory @1 (text :Text, parent :Text) -> (category: Text);
    getRootCategory @2 () -> (category: Category);
    registerUser @3 (user_id :Text) -> ();
    getChildCategories @4 (parent :Text) -> ( categories:List(Category));
    answer @5 (question : Text, user : Text, text : Text) -> (answer: Text);
    getAnswers @6 (question: Text) -> (answers: List(Answer) );
    voteQuestion @7 (question: Text, user :Text, vote :Int8) -> (rating: Int8);
    voteAnswer @8 (answer: Text, user :Text, vote :Int8) -> (rating: Int8);
    moveQuestion @9 (question: Text, category : Text);
}

struct Question {
    id @0 : Text;
    text @1 : Text;
    category @2 : Text;
}


struct Category {
    id @0 : Text;
    name @1: Text;
}

struct Answer {
    id @0 : Text;
    question @1 : Text;
    user @2 : Text;
    text @3 : Text;
}
