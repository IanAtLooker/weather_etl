require 'json'

def injest(filename) 
  File.open(filename) do |f|
    f.readlines.join('')
  end
end

HASHES = %w(
  image
  display_location
  observation_location
  estimated
)

HASH_KEYS = {
  'image' =>   ["url", "title", "link"],
  'display_location' => ["full", "city", "state", "state_name", "country", "country_iso3166", "zip", "magic", "wmo", "latitude", "longitude", "elevation"],
  'observation_location' => ["full", "city", "state", "country", "country_iso3166", "latitude", "longitude", "elevation"],
  'estimated' => []
}


STRINGS = %w(
  station_id observation_time observation_time_rfc822 observation_epoch local_time_rfc822 local_epoch local_tz_short local_tz_long local_tz_offset weather temperature_string
  relative_humidity wind_string wind_dir pressure_mb pressure_in pressure_trend dewpoint_string heat_index_string heat_index_f heat_index_c windchill_string windchill_f windchill_c 
  feelslike_string feelslike_f feelslike_c visibility_mi visibility_km solarradiation UV precip_1hr_string precip_1hr_in precip_1hr_metric precip_today_string
  precip_today_in precip_today_metric icon icon_url forecast_url history_url ob_url nowcast
)

ALL_KEYS = HASHES + STRINGS

def parse_json(json)
  parsed = JSON.parse(json)

  curr = parsed['current_observation']

  keys = []
  values = []

  (ALL_KEYS).each do |key|
    if (HASHES.include?(key)) 
      HASH_KEYS[key].each do |hkey|
        values << curr[key][hkey]
        keys << key + "_" + hkey         
      end
    else 
      values << curr[key]
      keys << key  
    end
  end
  return [keys, values]
end


json = injest('weather.json')
keys, values = parse_json(json)

#puts keys.join(',')
puts values.map{|s| "\"#{s}\""}.join(',')
