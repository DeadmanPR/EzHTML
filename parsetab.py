
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'DD20176F36C75CEED34F1B73F9527093'
    
_lr_action_items = {'TITLE':([0,],[1,]),'TEXT':([69,],[72,]),'DESTINATION':([57,94,],[60,97,]),'RP':([38,51,52,],[44,54,55,]),'WIDTH':([82,],[85,]),'LINK':([9,11,13,14,17,25,45,48,111,112,122,],[10,-9,-7,-10,-8,10,10,-11,-20,-21,-19,]),'LINKATTR':([35,],[41,]),'FONT':([74,],[77,]),'BOLD':([98,],[101,]),'CONSTANTVALUE':([34,56,68,80,87,104,114,118,],[40,59,71,83,90,107,115,119,]),'LB':([8,44,54,55,],[9,49,57,58,]),'SEMICOLON':([5,28,29,33,40,43,59,66,67,71,78,79,83,90,91,95,102,103,107,108,109,115,119,121,],[6,35,36,39,45,48,62,69,70,74,81,82,86,93,94,98,105,106,110,111,112,116,120,122,]),'COLOR':([49,],[53,]),'IMAGE':([9,11,13,14,17,25,45,48,111,112,122,],[12,-9,-7,-10,-8,12,12,-11,-20,-21,-19,]),'NUMERICVALUE':([76,88,92,99,],[79,91,95,102,]),'SOURCE':([58,],[61,]),'LP':([16,41,42,],[31,46,47,]),'UNDERLINE':([116,],[117,]),'$end':([2,3,7,39,],[-1,0,-2,-3,]),'BODY':([6,],[8,]),'STYLE':([9,11,13,14,17,25,45,48,111,112,122,],[16,-9,-7,-10,-8,16,16,-11,-20,-21,-19,]),'RB':([11,13,14,17,25,26,32,48,50,105,106,111,112,120,122,],[-9,-7,-10,-8,-4,33,-5,-11,-6,108,109,-20,-21,121,-19,]),'HEIGHT':([70,],[73,]),'PARAGRAPH':([9,11,13,14,17,25,45,48,111,112,122,],[18,-9,-7,-10,-8,18,18,-11,-20,-21,-19,]),'FONTSIZE':([86,93,],[89,96,]),'IMAGEATTR':([36,],[42,]),'STRINGVALUE':([4,37,63,64,75,100,],[5,43,66,67,78,103,]),'EQ':([1,27,30,53,60,61,65,72,73,77,84,85,89,96,97,101,113,117,],[4,34,37,56,63,64,68,75,76,80,87,88,92,99,100,104,114,118,]),'ID':([10,12,15,18,19,20,21,22,23,24,31,46,47,],[28,29,30,-18,-13,-14,-12,-17,-15,-16,38,51,52,]),'H2':([9,11,13,14,17,25,45,48,111,112,122,],[19,-9,-7,-10,-8,19,19,-11,-20,-21,-19,]),'H3':([9,11,13,14,17,25,45,48,111,112,122,],[20,-9,-7,-10,-8,20,20,-11,-20,-21,-19,]),'H1':([9,11,13,14,17,25,45,48,111,112,122,],[21,-9,-7,-10,-8,21,21,-11,-20,-21,-19,]),'H6':([9,11,13,14,17,25,45,48,111,112,122,],[22,-9,-7,-10,-8,22,22,-11,-20,-21,-19,]),'H4':([9,11,13,14,17,25,45,48,111,112,122,],[23,-9,-7,-10,-8,23,23,-11,-20,-21,-19,]),'H5':([9,11,13,14,17,25,45,48,111,112,122,],[24,-9,-7,-10,-8,24,24,-11,-20,-21,-19,]),'ITALIC':([110,],[113,]),'BACKGROUND_COLOR':([9,11,13,14,17,25,45,48,111,112,122,],[27,-9,-7,-10,-8,27,27,-11,-20,-21,-19,]),'ALIGNMENT':([62,81,],[65,84,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([6,],[7,]),'title':([0,],[2,]),'type_assignment':([9,25,45,],[13,13,13,]),'attr_definition':([9,25,45,],[17,17,17,]),'start':([0,],[3,]),'image_definition':([9,25,45,],[14,14,14,]),'statement':([9,25,45,],[25,25,25,]),'link_definition':([9,25,45,],[11,11,11,]),'statement_list':([9,25,45,],[26,32,50,]),'type':([9,25,45,],[15,15,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> title','start',1,'p_start','myParse.py',8),
  ('title -> TITLE EQ STRINGVALUE SEMICOLON body','title',5,'p_title','myParse.py',14),
  ('body -> BODY LB statement_list RB SEMICOLON','body',5,'p_body','myParse.py',20),
  ('statement_list -> statement','statement_list',1,'p_statement_list','myParse.py',25),
  ('statement_list -> statement statement_list','statement_list',2,'p_statement_list','myParse.py',26),
  ('statement_list -> BACKGROUND_COLOR EQ CONSTANTVALUE SEMICOLON statement_list','statement_list',5,'p_statement_list','myParse.py',27),
  ('statement -> type_assignment','statement',1,'p_statement','myParse.py',37),
  ('statement -> attr_definition','statement',1,'p_statement','myParse.py',38),
  ('statement -> link_definition','statement',1,'p_statement','myParse.py',39),
  ('statement -> image_definition','statement',1,'p_statement','myParse.py',40),
  ('type_assignment -> type ID EQ STRINGVALUE SEMICOLON','type_assignment',5,'p_type_assignment','myParse.py',45),
  ('type -> H1','type',1,'p_type','myParse.py',53),
  ('type -> H2','type',1,'p_type','myParse.py',54),
  ('type -> H3','type',1,'p_type','myParse.py',55),
  ('type -> H4','type',1,'p_type','myParse.py',56),
  ('type -> H5','type',1,'p_type','myParse.py',57),
  ('type -> H6','type',1,'p_type','myParse.py',58),
  ('type -> PARAGRAPH','type',1,'p_type','myParse.py',59),
  ('attr_definition -> STYLE LP ID RP LB COLOR EQ CONSTANTVALUE SEMICOLON ALIGNMENT EQ CONSTANTVALUE SEMICOLON FONT EQ CONSTANTVALUE SEMICOLON FONTSIZE EQ NUMERICVALUE SEMICOLON BOLD EQ CONSTANTVALUE SEMICOLON ITALIC EQ CONSTANTVALUE SEMICOLON UNDERLINE EQ CONSTANTVALUE SEMICOLON RB SEMICOLON','attr_definition',35,'p_attr_definition','myParse.py',64),
  ('link_definition -> LINK ID SEMICOLON LINKATTR LP ID RP LB DESTINATION EQ STRINGVALUE SEMICOLON TEXT EQ STRINGVALUE SEMICOLON ALIGNMENT EQ CONSTANTVALUE SEMICOLON FONTSIZE EQ NUMERICVALUE SEMICOLON RB SEMICOLON','link_definition',26,'p_link_definition','myParse.py',76),
  ('image_definition -> IMAGE ID SEMICOLON IMAGEATTR LP ID RP LB SOURCE EQ STRINGVALUE SEMICOLON HEIGHT EQ NUMERICVALUE SEMICOLON WIDTH EQ NUMERICVALUE SEMICOLON DESTINATION EQ STRINGVALUE SEMICOLON RB SEMICOLON','image_definition',26,'p_image_definition_error','myParse.py',87),
]