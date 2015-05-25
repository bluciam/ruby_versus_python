require_relative 'test'

def replace(matrix)
  new_matrix = matrix
  zeroes = find_da_zeros(matrix)
  zeroes.each do |zero|
    matrix.each_with_index do |row, x|
      if x == zero[:x]
        row.each_with_index do |val, y|
          row[y] = 0
        end
      else
        row[zero[:y]] = 0
      end
    end
  end
  new_matrix
end

def find_da_zeros(matrix)
  zeroes = []
  matrix.each_with_index do |row, x|
    row.each_with_index do |pixel, y|
      if pixel == 0
        zeroes.push({x: x, y: y})
      end
    end
  end
  zeroes
end


test(replace(
         [
             [1,1,1,1,1],
             [1,1,1,0,1],
             [1,1,1,1,1],
             [1,1,1,1,1],
             [1,1,1,1,1]
         ]),
     [
         [1,1,1,0,1],
         [0,0,0,0,0],
         [1,1,1,0,1],
         [1,1,1,0,1],
         [1,1,1,0,1]
     ]
) # 5x6 image

puts ""