function solution(str1, str2) {
  const ordA = 'a'.charCodeAt(0)
  const ordZ = 'z'.charCodeAt(0)
  const set1 = makeSet(str1.toLowerCase(), ordA, ordZ)
  const set2 = makeSet(str2.toLowerCase(), ordA, ordZ)
  
  return parseInt(similarity(set1, [...set2]) * 65536);
}


function makeSet(string, ordA, ordZ) {
  const multiSet = []
  for (let i = 0; i < string.length - 1; i++) {
    const char1 = string[i]
    const char2 = string[i+1]
    if ((ordA <= char1.charCodeAt(0) && char1.charCodeAt(0) <= ordZ) && (ordA <= char2.charCodeAt(0) && char2.charCodeAt(0) <= ordZ)) {
      multiSet.push(char1 + char2)
    }
  }
  return multiSet
}


function similarity(set1, set2) {
  const visited1 = new Array(set1.length).fill(0)
  const visited2 = new Array(set2.length).fill(0)

  // 교집합
  for (let i = 0; i < set1.length; i++) {
    const char1 = set1[i]
    for (let j = 0; j < set2.length; j++) {
      const char2 = set2[j]
      if (visited2[j]) continue
      if (char1 === char2) {
        visited1[i] = 1
        visited2[j] = 1
        break
      }
    }
  }
  const intersection = set1.filter((v, i) => visited1[i])

  // 합집합
  const union = set1.concat(set2)
  for (const char of intersection) {
    const idx = union.indexOf(char)
    union.splice(idx, 1)
  }
  if (!union.length) return 1
  return intersection.length / union.length
}


const dataset = [
  ['FRANCE', 'french'],
  ['handshake', 'shake hands'],
  ['aa1+aa2', 'AAAA12'],
  ['E=M*C^2', 'e=m*c^2'],
]


for (const [str1, str2] of dataset) {
  console.log(solution(str1, str2))
}