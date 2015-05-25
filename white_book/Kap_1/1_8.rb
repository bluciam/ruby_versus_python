require_relative 'test'

def is_rotation?(s1, s2)
  test_string = s2 + s2
  test_string.include? s1
end



test(is_rotation?('qwerty', 'tyqwer'), true)
test(is_rotation?('waterbottle', 'erbottlewat'), true)
test(is_rotation?('qwerty', 'ytrewq'), false)


puts ""