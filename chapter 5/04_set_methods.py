# 1. add()
a = {64, 85, 93.4, "Abdullah"}
a.add("Ayesha") # will add an element to the set
print(a)

# 2. update()
b = {1, 2}
b.update([3, 4])  # Adds multiple elements from iterable (list, set, etc.)
print(b)

# 3. remove()
c = {1, 2, 3}
c.remove(2)  # Removes 2 from set; raises KeyError if 2 not found
print(c)

# 4. discard()
d = {1, 2, 3}
d.discard(4)  # Removes 4 if present; does nothing if not (no error)
print(d)

# 5. pop()
e = {10, 20, 30}
e.pop()  # Removes and returns a random element; raises KeyError if empty
print(e)

# 6. clear()
f = {1, 2, 3}
f.clear()  # Removes all elements, making the set empty
print(f)

# 7. union()
g = {1, 2}
h = {2, 3}
union = g.union(h)  # Returns a new set with all elements from both
print(union)

# 8. intersection()
i = {1, 2, 3}
j = {2, 3, 4}
result = i.intersection(j)  # Returns elements common to both sets
print(result)

# 9. difference()
k = {1, 2, 3}
l = {2, 3, 4}
differ = k.difference(l)  # Elements in k but not in l → {1}
print(differ)

# 10. symmetric_difference()
m = {1, 2, 3}
n = {3, 4, 5}
ans = m.symmetric_difference(n)  # Elements in either set, but not both → {1, 2, 4, 5}
print(ans)

# 11. issubset()
o = {1, 2}
p = {1, 2, 3}
o.issubset(p)  # Returns True if all elements of o are in p
print(o)

# 12. issuperset()
q = {1, 2, 3}
r = {2, 3}
q.issuperset(r)  # Returns True if q contains all elements of r
print(q)

# 13. isdisjoint()
s = {1, 2}
t = {3, 4}
s.isdisjoint(t)  # True if no common elements
print(s)

# These are some of the most important methods in sets.