function solution(m, n, board) {
  let answer = 0;
  board = board.map(item => item.split(''))
  let flag = true
  while (flag) {
    flag = false
    board, flag = break_block(m, n, board, flag)
    board = sort_block(m, n, board)
  }

  return count_block(m, n, board, answer);
}


function break_block(m, n, board, flag) {
  let broken = []
  for (let r = 0; r < m-1; r++) {
    for (let c = 0; c < n-1; c++) {
      if (board[r][c] === '.') continue
      if (board[r][c] === board[r+1][c] && board[r][c] === board[r+1][c+1] && board[r][c] === board[r][c+1]) {
        broken = broken.concat([[r, c], [r+1, c], [r, c+1], [r+1, c+1]])
        flag = true
      }
    }
  }
  while (broken.length) {
    const [r, c] = broken.pop()
    board[r][c] = '.'
  }
  return board, flag
}


function sort_block(m, n, board) {
  for (let c = 0; c < n; c++) {
    for (let r = m-1; r > 0; r--) {
      // console.log(r, c, board[r][c])
      let rr = r
      let end = false
      if (board[r][c] === '.') {
        end = true
        // console.log('roop')
        while (true) {
          rr -= 1
          if (rr < 0) break
          if (board[rr][c] !== '.') {
            board[r][c] = board[rr][c]
            board[rr][c] = '.'
            end = false
            break
          }
        }
      }
      if (end) break
    }
  }
  return board
}


function count_block(m, n, board, answer) {
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (board[r][c] === '.') answer += 1
    }
  }
  return answer
}

const dataset = [
  [4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']],
  [6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']]
]

for (let [m, n, board] of dataset) {
  console.log(solution(m, n, board))
  // break
}