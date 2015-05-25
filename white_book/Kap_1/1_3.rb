require_relative 'test'

def permutation?(string, other_string)
  string.chars.each do |char|
    if string.count(char) != other_string.count(char)
      return false
    end
  end
  true
end

test(permutation?('qwerty', 'ytrewq'), true)
test(permutation?('hello world', 'bye!'), false )

puts ""