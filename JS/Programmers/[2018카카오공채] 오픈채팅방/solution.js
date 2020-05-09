function solution(record) {
  const answer = [];
  const result = []
  const nickname = {}
  record = record.map(item => item.split(' '))
  for (const item of record) {
    if (item[0] === 'Enter') {
      answer.push(item[1])
      answer.push('님이 들어왔습니다.')
      nickname[item[1].toString()] = item[2]
    } 
    else if (item[0] === 'Leave') {
      answer.push(item[1])
      answer.push('님이 나갔습니다.')
    }
    else if (item[0] === 'Change') {
      nickname[item[1].toString()] = item[2]
    }
  }
  for (let i = 0; i < answer.length; i += 2) {
    answer[i] = nickname[answer[i].toString()]
  }
  for (let i = 0; i < answer.length; i += 2) {
    const message = answer[i] + answer[i+1]
    result.push(message)
  }
  
  return result;
}

const dataset = [
  ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
]

for (let record of dataset) {
  console.log(solution(record))
}