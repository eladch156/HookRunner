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
OpenParanthesis : '(';
CloseParanthesis : ')';
OpenAngleBrackets: '<';
CloseAngleBrackets: '>';
FreeText: '"' ~["]*? '"';
Equals : '=';
End: ';';
NewLine: ('\r' '\n'? | '\n');
Identifier: [a-zA-Z] [a-zA-Z0-9_\-]*;
Digits: [0-9]+;




// Primary
primaryExpression: (BlockComment | LineComment | variableDeclare | includeSentence | functionCall)+;
sentenceEnding: End | NewLine | EOF;
includeSentence: Include OpenAngleBrackets Identifier Dot Identifier CloseAngleBrackets sentenceEnding;
variableDeclare: Declare Identifier Equals FreeText sentenceEnding;
argument: Identifier | FreeText | Digits;
arguments : (argument  ',' )* argument;
functionCall: (Identifier Dot)? Identifier '(' arguments? ')' sentenceEnding;