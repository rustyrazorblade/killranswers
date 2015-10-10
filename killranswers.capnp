@0xce4c7cd66480f6f2;

interface KillrAnswers {
    ask @0 (text :Text, category :Text, user :Text) -> (question: Text);
    createCategory @1 (text :Text, parent :Text) -> (category: Text);
    getRootCategory @2 () -> (category: Category);
    registerUser @3 (userId :Text);
    answer @4 (question : Text, user : Text, text : Text) -> (answer: Text);
    voteQuestion @5 (question: Text, user :Text, vote :Int8) -> (rating: Int8);
    voteAnswer @6 (question: Text, answer: Text, user :Text, vote :Int8) -> (rating: Int8);
    moveQuestion @7 (question: Text, category : Text);
    getAnswers @8 (question: Text) -> (answers: List(Answer) );
    getChildCategories @9 (parent :Text) -> ( categories:List(Category));
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
