function solution(s) {
  const answer = [];
  const visited = new Object
  const order = new Array
  let idx = 0
  let num = ''
  for (let char of s) {
    if (char === '{' | char === '}' | char === ',') {
      if (num !== '') {
        if (visited[num] === undefined) {
          visited[num] = idx
          idx += 1
          order.push(0)
        }
        order[visited[num]] += 1
      } 
      num = ''
    } else {
      num += char
    }
  }
  const arr_length = order.length
  for (let key in visited) {
    const idx = visited[key]
    answer[arr_length - order[idx]] = key
  }
  
  return answer.map(num => Number(num));
}

dataset = [
  "{{2},{2,1},{2,1,3},{2,1,3,4}}",
  "{{1,2,3},{2,1},{1,2,4,3},{2}}",
  "{{20,111},{111}}",
  "{{123}}",
  "{{4,2,3},{3},{2,3,4,1},{2,3}}",
]

for (let i = 0; i < dataset.length; i++) {
  console.log(solution(dataset[i]))
  // break
}
