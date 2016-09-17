def add(a1, a2):
	return map(lambda x,y : x+y, a1, a2)

def mul(a1, k):
	return [i*k for i in a1]

class Matrix:
	def __init__(self, M):
		self.M = M
		self.length = len(M)

	def get_line(self, n):
		return self.M[n]

	def set_line(self, line, n):
		self.M[n] = line

	def get_column(self, n):
		column = []
		for i in M:
			column.append(i[n])
		return column

	def swap_lines(self, n1, n2):
		line1 = self.get_line(n1)
		line2 = self.get_line(n2)
		self.M[n1] = line2
		self.M[n2] = line1
		return True

	def add_line(self, sink_num, sourse_num, k):
		sink = self.get_line(sink_num)
		sourse = self.get_line(sourse_num)
		sourse = mul(sourse, k)
		sink = add(sink, sourse)
		self.set_line(sink, sink_num)

	def mul_line(self, sink_num, k):
		sink = self.get_line(sink_num)
		sink = mul(sink, k)
		self.set_line(sink, sink_num)


	def __str__(self):
		string = ""
		for i, item in enumerate(self.M):
			kefal = str(item[0:-1])
			string += kefal[1:-1] + " | " + str(item[-1])
			string += "\n"
		return string

	def go_triangular(self, iterations=0):
		if iterations == 3:
			return None
		M = self.M[iterations:]

		def sort_by_step(n):
			step = n
			def sort_by_mechanic(row):
				return abs(row[step])
			return sort_by_mechanic

		M.sort(key=sort_by_step(iterations), reverse=True)
		t_matrix = Matrix(M)
		t_matrix.mul_line(0, 1.0 / M[0][0])
		for i in range(1, t_matrix.length):
			t_matrix.add_line(i, 0, -M[i][0])

		print str(t_matrix)

