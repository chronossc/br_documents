br_documents
============

Provide objects for brazilian documents like RG, CPF, CNPJ and others, with validation

CPF
===

Represents a CPF. Raises a InvalidCPF error when it is invalid.

	>>> from br_documents import CPF
	>>> a = CPF(87234238115)
	>>> a
	<CPF: 87234238115>
	>>> str(a) == '87234238115'
	True
	>>> b = CPF('29057139332')
	>>> c = CPF(29057139332)
	>>> d = CPF('290.571.393-32')
	>>> b == c, b == d
	(True, True)
	>>> c.formated == '290.571.393-32'
	True


