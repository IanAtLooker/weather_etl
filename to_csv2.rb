require 'json'

def injest(filename) 
  File.open(filename) do |f|
    f.readlines.join('')
  end
end

HASHES = %w(
  date 
  utcdate
  observations
  daily summary
)

HASH_KEYS = {
  'date' =>   ["pretty","year","mon","mday","hour","min","tzname"],
  'utcdate' => ["pretty","year","mon","mday","hour","min","tzname"],
  'observation' => [],
  'dailysummary' => ["pretty","year","mon","mday","hour","min","tzname"]
}


STRINGS = %w(
og rain snow snowfallm snowfalli monthtodatesnowfallm monthtodatesnowfalli since1julsnowfallm since1julsnowfalli snowdepthm snowdepthi hail thunder tornado meantempm meantempi meandewptm meandewpti meanpressurem meanpressurei meanwindspdm meanwindspdi meanwdire meanwdird meanvism meanvisi humidity maxtempm maxtempi mintempm mintempi maxhumidity minhumidity maxdewptm maxdewpti mindewptm mindewpti maxpressurem maxpressurei minpressurem minpressurei maxwspdm maxwspdi minwspdm minwspdi maxvism maxvisi minvism gdegreedays heatingdegreedays coolingdegreedays precipm precipi precipsource heatingdegreedaysnormal monthtodateheatingdegreedays monthtodateheatingdegreedaysnormal since1sepheatingdegreedays since1sepheatingdegreedaysnormal since1julheatingdegreedays since1julheatingdegreedaysnormal coolingdegreedaysnormal monthtodatecoolingdegreedays monthtodatecoolingdegreedaysnormal since1sepcoolingdegreedays since1sepcoolingdegreedaysnormal since1jancoolingdegreedays since1jancoolingdegreedaysnormal
)

ALL_KEYS = HASHES + STRINGS

def parse_json(json)
  parsed = JSON.parse(json)

  curr = parsed['history']

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


json = injest('hist_weather.json')
keys, values = parse_json(json)

puts keys.join(',')
puts values.map{|s| "\"#{s}\""}.join(',')
