require_relative 'test'

def reverse(string)
  new_string = ""
  string.chars.each do |char|
    new_string = char << new_string
  end
  new_string
end

test(reverse('qwerty'), 'ytrewq')
test(reverse('hello world'), 'dlrow olleh' )

puts ""