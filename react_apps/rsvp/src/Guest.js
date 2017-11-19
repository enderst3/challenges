import React from 'react';
import PropTypes from 'prop-types';
import GuestName from './GuestName';

const Guest = props => 
 
  <li>
    <GuestName 
      isEditing={props.isEditing}
      handleNameEdits={e => props.setName(e.target.value)}>
      {props.name}
    </GuestName>
    <label>
      <input 
        type="checkbox" 
        checked={props.isConfirmed} 
        onChange={props.handleConfirmation}
      /> Confirmed
    </label>
    <button onClick={props.handleToggleEditing}>
      {props.isEditing ? 'save' : 'edit'}
    </button>
    <button onClick={props.handleRemove}>remove</button>
  </li>

Guest.PropTypes = {
  name: PropTypes.string,
  isConfirmed: PropTypes.bool,
  isEditing: PropTypes.bool,
  setName: PropTypes.func,
  handleConfirmation: PropTypes.func,
  handleToggleEditing: PropTypes.func,
  handleRemove: PropTypes.func
}

export default Guest;