grammar HookRunnerLang;

//Tokens
IF: 'IF';
WS:[ \t\r\n]+ -> skip;
NAME: [a-zA-Z_]+;
CONDITION_OPERATOR: '>' | '<' | '>=' | '<=' | '==';
THEN: 'Then';
END: 'End';
IMPORT: 'Import';
LET: 'Let';
NUMBER: ('0' | [1-9][0-9]*);
STRING: '"' .*? '"';
EQUALS_SIGN: '=';



//Compound
start: sentence;
sentence: ((condition | command) ';') + ;
name: NAME;
value: STRING | NUMBER;
lib: IMPORT name;
variable: LET name EQUALS_SIGN value;
condition: IF '[' (variable | value) CONDITION_OPERATOR (variable | value) ']' THEN sentence END;
args: ((name ',')* name);
command: name '.' name '(' args ')' | name '(' args ')' | name '(' ')';
