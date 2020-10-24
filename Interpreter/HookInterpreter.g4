grammar HookInterpreter;
// ######## Version 0.0.1 #############//
// Skip
Whitespace: [ \t]+ -> skip;
BlockComment: '/*' .*? '*/' -> skip;
LineComment: '//' ~[\r\n]* NewLine  -> skip;


// Tokens
Declare : 'Declare';
Include : 'Include';
Dot: '.';
DoubleDot: '..';
AssigmentOpreator :  ('=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|=');
OpenParanthesis : '(';
CloseParanthesis : ')';
OpenAngleBrackets: '<';
CloseAngleBrackets: '>';
FreeText: '"' ~["]*? '"';
End: ';';
NewLine: ('\r' '\n'? | '\n');
Identifier: [a-zA-Z] [a-zA-Z0-9_\-]*;
Digits: [0-9]+;




// Primary
primaryExpression: ( BlockComment | LineComment | singleFunctionCall | multiAssingment | includeSentence)+;
ending: End | NewLine | EOF;
includeSentence: Include OpenAngleBrackets Identifier Dot Identifier CloseAngleBrackets ending;
value: (Identifier | FreeText | Digits);
multiAssingment: (assigmentWithOutDecl | assigmentWithDecl) (',' assigmentWithOutDecl)* ending;
assigmentWithOutDecl: value AssigmentOpreator (functionCall | value);
assigmentWithDecl: Declare assigmentWithOutDecl;
functionCall: (Identifier Dot)? Identifier '(' values? ')';
singleFunctionCall: functionCall ending;
values : (value  ',' )* value;