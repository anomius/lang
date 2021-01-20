#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
#########################################################
#########################################################
################         TOKENS        ##################
#########################################################
#########################################################

TT_INT		= 'INT'
TT_FLOAT    = 'FLOAT'
TT_PLUS     = 'PLUS'
TT_MINUS    = 'MINUS'
TT_MUL      = 'MUL'
TT_DIV      = 'DIV'
TT_LPAREN   = 'LPAREN'
TT_RPAREN   = 'RPAREN'







class tokens:
    def __init__(self,type_,value_) -> None:
        self.type=type_
        self.value=value_
    
    def __repr__(self) -> str:
        if self.value: return f'{self.type}:{self.value}'
        else: return f'{self.type}'




#########################################################
#########################################################
################          LEXER        ##################
#########################################################
#########################################################

class lexer:
    def __init__(self,text) -> None:
        self.text=text 
        self.pos=-1
        self.curr_char=None
        self.advance()

    def advance(self):
        self.pos+=1
        self.curr_char=self.text[self.pos] if self.pos<len(self.text) else None

    def tokenize(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None
        return tokens
