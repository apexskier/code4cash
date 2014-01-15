DEG_PER_HOUR = (360.to_f / 12)
# puts DEG_PER_SEC
DEG_PER_MIN = (360.to_f / 60)
DEG_PER_SEC = DEG_PER_MIN

file = File.new("SampleInput.txt", "r")
lines = file.readlines


file.close

# puts lines.inspect

count = lines.shift

lines.map! do |line|
  hour = line[0..1]
  minute = line[3..4]
  second = line[6..7]
  # puts "#{hour}:#{minute}:#{second}"
  hour_angle = (hour.to_f * DEG_PER_HOUR) + (DEG_PER_HOUR/60)*minute.to_f + (DEG_PER_HOUR/60/60)*second.to_f
  minute_angle = (minute.to_f * DEG_PER_MIN) + (DEG_PER_MIN/60)*second.to_f
  second_angle = second.to_f * DEG_PER_SEC

  # puts "#{hour_angle}, #{minute_angle}"


  hour_min = (hour_angle - minute_angle).abs
  # puts hour_min
  if hour_min.abs > 180
    hour_min = (360 - hour_min.abs).abs
  end

  hour_sec = (hour_angle - second_angle).abs
  if hour_sec.abs > 180
    hour_sec = (360 - hour_sec.abs).abs
  end

  min_sec = (minute_angle - second_angle).abs
  if min_sec.abs > 180
    min_sec = (360 - min_sec.abs).abs
  end

  "#{hour_min.round(2)}, #{hour_sec.round(2)}, #{min_sec.round(2)}"

end


file = File.new("Output.txt", "w")
lines.each do |line|
  file.puts line
end

file.close