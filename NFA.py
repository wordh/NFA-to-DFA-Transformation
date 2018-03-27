class NFA: 
	"""Class that encapsulates an NFA."""
	def __init__(self, transitionFunction, initialState, finalStates):
		self.delta = transitionFunction	
		self.q0 = initialState
		self.F = set(finalStates)
	def deltaHat(self, state, inputString):
		"""deltaHat is smart enough to return the empty set if no transition is defined."""
		states = set([state])
		for a in inputString: 
			newStates = set([])
			for state in states: 
				try: 
					newStates = newStates | self.delta[state][a]
				except KeyError: pass
			states = newStates
		return states
	def inLanguage(self, inputString):
		return len(self.deltaHat(self.q0, inputString) & self.F) > 0
	def alphabet(self):
		"""Returns the NFA's input alphabet, generated on the fly."""
		Sigma = reduce(lambda a,b:set(a)|set(b), [x.keys() for x in N.delta.values()])
		return Sigma
	def states(self):
		"""Returns the NFA's set of states, generated on the fly."""
		Q = set([self.q0]) | set(self.delta.keys()) | reduce(lambda a,b:a|b, reduce(lambda a,b:a+b, [x.values() for x in self.delta.values()]))	# {q0, all states with outgoing arrows, all with incoming arrows}
		return Q

#Here NFA is made with all possible routes
delta = {'q0':{'0':set(['q0','q1']),'1':set(['q0'])}, 'q1':{'0':set(['q2'])}}
N = NFA(delta, 'q0', ['q2'])
N.deltaHat('q0', '0001')
print [(x, N.inLanguage(x)) for x in ['0100', '00010', '10010100']]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
