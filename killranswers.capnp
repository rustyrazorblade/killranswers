@0xce4c7cd66480f6f2;

interface KillrAnswers {
    ask @0 (i :Text) -> (questionId: Text);
}

struct Question {
    questionId @0 : Text;
    questionText @1 : Text;
}

struct Category {
    categoryId @0 : Text;
}
