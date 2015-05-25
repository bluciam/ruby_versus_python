require_relative 'test'

def rotate(image)
  new_image = Array.new
  cols_nbr = image.first.count
  cols_nbr.times do
    new_image.push []
  end
  image.each do |row|
    row.each_with_index do |pixel, y|
     new_image[cols_nbr - y -1].push pixel
    end
  end
  new_image
end


test(rotate(
      [
        [1,2,3,4,5],
        [3,4,6,2,8],
        [4,2,8,6,4],
        [3,6,3,7,4],
        [2,6,7,2,5],
        [2,6,3,5,0]
      ]),
      [
        [5,8,4,4,5,0],
        [4,2,6,7,2,5],
        [3,6,8,3,7,3],
        [2,4,2,6,6,6],
        [1,3,4,3,2,2]
      ]
) # 5x6 image

puts ""