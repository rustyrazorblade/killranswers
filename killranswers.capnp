@0xce4c7cd66480f6f2;

interface KillrAnswers {
    ask @0 (text :Text) -> (question: Question);
    createCategory @1 (name: Text, parent: Text) -> (category: Category);
    getRootCategory @2 () -> (category: Category);
}

struct Question {
    questionId @0 : Text;
    questionText @1 : Text;
}

struct Category {
    categoryId @0 : Text;
    name @1: Text;
}
