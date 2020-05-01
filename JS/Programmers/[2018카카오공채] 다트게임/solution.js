function solution(dartResult) {
  const answer = 0;
  const scoreBoard = []
  let num = ''
  let idx = -1
  for (const char of dartResult) {
    if (!(char === 'S'|char === 'D'|char === 'T'|char === '*'|char === '#')) {
      num += char
    } else {
      if (num.length !== 0) {
        idx += 1
        scoreBoard.push(parseInt(num))
        num = ''
      }

      if (char === 'D') {
        scoreBoard[idx] **= 2
      } else if (char === 'T') {
        scoreBoard[idx] **= 3
      } else if (char === '*') {
        if (idx !== 0) {
          scoreBoard[idx] *= 2
          scoreBoard[idx-1] *= 2
        } else {
          scoreBoard[idx] *= 2
        }
      } else if (char === '#') {
        scoreBoard[idx] *= (-1)
      }
    }
  }
  return scoreBoard.reduce((val, cur) => val + cur);
}
const dataset = [
  '1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*'
]

for (const dartResult of dataset) {
  console.log(solution(dartResult))
  // break
}
