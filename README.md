# rollup-bot
Bot to check [zkRollup](https://github.com/iden3/rollup/blob/testnet/README.md) state.
It sends notifications automatically to a riot room if:
  - Cannot get state information
  - Batch forged has not increased correctly
  - New account is added

## Config
### Matrix
`server`: matrix url server
`user`: user name
`pass`: user password
`roomId`: matrix room identifier

### Rollup
`url`: rollup url
`lastAccount`: last account found

### Example
```json
{
  "matrix": {
    "server": "https://matrix.org",
    "user": "matrixUser",
    "pass": "passphrase",
    "roomId": "!rommId:matrix.org"
  },
  "rollup": {
    "url": "https://zkrollup.iden3.net",
    "lastAccount": 23
  }
}
```

## Requirements
matrix_client
requests
time
sys
pathlib

## Run service
`python3 main.py`
