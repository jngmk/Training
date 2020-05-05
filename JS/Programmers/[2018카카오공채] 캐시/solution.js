function solution(cacheSize, cities) {
  let answer = 0;
  const caches = new Array(cacheSize)
  for (let city of cities) {
    city = city.toLowerCase()
    let isCache = false
    let subtitute = cacheSize-1
    for (let i = 0; i < cacheSize; i++) {
      if (city === caches[i]) {
        answer += 1
        isCache = true
        subtitute = i
        break
      }
    }
    if (!isCache) answer += 5

    for (let i = subtitute; i > 0; i--) {
      caches[i] = caches[i-1]
    }
    caches[0] = city
  }
  return answer;
}


const dataset = [
  [3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']],

]

for (const [cacheSize, cities] of dataset) {
  console.log(solution(cacheSize, cities))
}