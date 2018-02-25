import { FETCH_WEATHER } from '../actions/index'

export default function(state = [], action) {
  switch (action.type) {
  case FETCH_WEATHER:
    // creates new array not manipulating existing array
    return [ action.payload.data, ...state ]
  }
  return state
}