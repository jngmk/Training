let subkeyArr = []

function solution(relation) {
  let combinations = []
  let subkeys = []
  for (let i = 1; i < relation.length + 1; i++) {
    
    comb(0, i, relation[0].length, 0, [])
    combinations = combinations.concat(subkeyArr)
    subkeyArr = []
  }

  for (const item of combinations) {
    // 최소성 만족
    let flag = false
    if (subkeys.length) {
      for (const subkey of subkeys) {
        const intersect = item.filter(v => subkey.includes(v))
        if (intersect.length === subkey.length) {
          flag = true
          break
        }
        if (flag) break
      }
    }
    if (flag) continue
    // 유일성 만족
    const values = {}
    for (const data of relation) {
      const value = []
      for (const i of item) {
        value.push(data[i])
      }
      values[value] = 1
    }
    if (Object.keys(values).length === relation.length) {
      subkeys.push(item)
    }
  }
  return subkeys.length;
}


function comb(k, depth, length, now, subkey) {
  if (k == depth) {
    subkeyArr.push([...subkey])
    return
  }
  for (let j = now; j < length; j++) {
    subkey.push(j)
    comb(k+1, depth, length, j+1, subkey)
    subkey.pop()
  }
}

dataset = [
  [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
  ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]],
]

for (const relation of dataset) {
  console.log(solution(relation))
}