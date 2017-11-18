import React from 'react';
import PropTypes from 'prop-types';
import GuestName from './GuestName';

const Guest = props => 
 
  <li>
    <GuestName isEditing={props.isEditing}>
      {props.name}
    </GuestName>
    <label>
      <input 
        type="checkbox" 
        checked={props.isConfirmed} 
        onChange={props.handleConfirmatiohn}
      /> Confirmed
    </label>
    <button onClick={props.handleToggleEditing}>edit</button>
    <button>remove</button>
  </li>

Guest.PropTypes = {
  name: PropTypes.string,
  isConfirmed: PropTypes.bool,
  isEditing: PropTypes.bool,
  handleConfirmation: PropTypes.func,
  handleToggleEditing: PropTypes.func
}

export default Guest;