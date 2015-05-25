require_relative 'test'

def unique_characters?(string)
  string.chars.each do |char|
    if string.count(char) != 1
      return false
    end
  end
  true
end

test(unique_characters?("asdfghjk"), true)
test(unique_characters?("aasdfghjk"), false )
test(unique_characters?("asdfghjkkk"), false )
test(unique_characters?("asdfghjk346"), true )

puts ""