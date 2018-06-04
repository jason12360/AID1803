def getfn():
	def print_hello():
		print('hello')
	return print_hello

fn = getfn()
fn()