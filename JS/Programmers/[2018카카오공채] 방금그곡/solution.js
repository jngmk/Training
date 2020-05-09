function solution(m, musicinfos) {
  const answer = []
  const remember = preprocess(m)
  let idx = 0
  for (const musicinfo of musicinfos) {
    idx += 1
    const [s, e, name, content] = musicinfo.split(',')
    const [sh, sm] = s.split(':').map(v => parseInt(v))
    const [eh, em] = e.split(':').map(v => parseInt(v))
    const length = (eh - sh) * 60 + (em - sm)
    
    const contentList = preprocess(content)
    const contentLength = contentList.length
    
    const repeat = parseInt(length / contentLength)
    const remain = length % contentLength
    
    let fullContent = []
    for (let i = 0; i < repeat; i++) {
      fullContent = fullContent.concat(contentList)
    }
      
    const remains = contentList.slice(0, remain)
    if (remains.length) {
      fullContent = fullContent.concat(remains)
    }
    for (let i = 0; i < fullContent.length; i++) {
      let compareContent = fullContent.slice(i, i+remember.length)
      if (remember.toString() === compareContent.toString()) {
        answer.push([length, idx, name])
        break
      }
    }
  }
  if (answer.length) {
    return answer.sort((a, b) => {
      if (a[0] > b[0]) return -1
      if (a[0] < b[0]) return 1
      if (a[1] < b[1]) return -1
    })[0][3]
  }
  return '(None)'
}


function preprocess(content) {
  const result = []
  for (let i = 0; i < content.length; i++) {
    if (content[i+1] === '#') {
      result.push(content.slice(i, i+2))
      i += 1
    }
    else {
      result.push(content.slice(i, i+1))
    }
  }
  return result
}


const dataset = [
  ['ABCDEFG', ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']],
  ['CC#BCC#BCC#BCC#B', ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']],
  ['ABCDEF', ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']]
]

for (const[m, musicinfos] of dataset) {
  console.log(solution(m, musicinfos))
  // break
}