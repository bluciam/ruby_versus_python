require_relative 'test'

def compress(string)
  compressed = ""
  chain = {char:'', nbr:1}
  (string + '/').chars.each do |char|
    if char == chain[:char]
      chain[:nbr] += 1
    else
      compressed << chain[:char]
      compressed << chain[:nbr].to_s if chain[:nbr] >= 2
      chain = {char:char, nbr:1}
    end
  end
  compressed.length == string.length ? string : compressed
end

test(compress('qwerty'), 'qwerty')
test(compress('hello world'), 'hello world')
test(compress('hello worldddd'), 'hel2o world4')
test(compress('hello wooooorld'), 'hel2o wo5rld')

puts ""