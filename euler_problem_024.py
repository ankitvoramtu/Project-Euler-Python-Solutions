
import itertools, sys
if sys.version_info.major == 2:
	range = xrange


def compute():
	arr = list(range(10))
	temp = itertools.islice(itertools.permutations(arr), 999999, None)
	return "".join([str(x) for x in next(temp)])


if __name__ == "__main__":
	print(compute())
