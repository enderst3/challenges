import React from 'react';
import PropTypes from 'prop-types';
import Guest from './Guest';

const GuestList = props => 
  <ul>
    {props.guests.map((guest, index) => 
      <Guest 
        key={index} 
        name={guest.isConfirmed}
        isConfirmed={guest.isConfirmed}
        isEditing={guest.isEditing}
        handleConfirmation={() => props.toggleConfirmationAt(index)}
        handleToggleEditing={() => props.toggleEditingAt(index)}
      />
    )} 
  </ul>
GuestList.PropTypes = {
  guests: PropTypes.array,
  toggleConfirmationAt: PropTypes.func,
  toggleEditingAt: PropTypes.func
}

export default GuestList;