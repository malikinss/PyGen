Lesson 5.9: object hashing (part 1)

Hashing
Applications of hashing
Built-in function hash()
Narrowing the range of hash values
Characteristics of a good hash function
Creating your own hash function
Abstract: This lesson is about hashing objects.

https://stepik.org/lesson/886253/step/1?unit=890908

This lesson has good theory explonation, 2 programing practical tasks and 21 theoretical questions presented on the website.

1. 5_9_1_hash_function

```
# hash_function Custom Object Hasher
The `hash_function` computes a custom hash value for any object by processing its string representation through a three-step algorithm.
First, it calculates the sum of products of symmetrically paired characters’ Unicode values (first with last, second with second-to-last, etc.), adding the middle character for odd-length strings.
Second, it computes an alternating weighted sum of Unicode values multiplied by their 1-based positions.
Finally, it multiplies these two results and takes the modulus with `123456791`, returning the final hash as an integer.
This function is designed for generating consistent hash values for objects, suitable for custom hashing in data structures, testing unique object signatures, or educational exercises exploring hash algorithms.
Its unique combination of symmetric pairing and alternating weights makes it a distinctive tool for applications needing deterministic yet complex hash computations, such as checksums or lightweight object fingerprinting.
```

2.

```

```
