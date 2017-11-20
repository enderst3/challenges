import React from 'react';
import PropTypes from 'prop-types';
import Guest from './Guest';
import PendingGuest from './PendingGuest'

const GuestList = props => 
  <ul>
    <PendingGuest name={props.pendingGuest} />
    {props.guests
      .filter(guest => !props.isFiltered || guest.isConfirmed)
      .map((guest, index) => 
        <Guest 
          key={index} 
          name={guest.name}
          isConfirmed={guest.isConfirmed}
          isEditing={guest.isEditing}
          handleConfirmation={() => props.toggleConfirmationAt(index)}
          handleToggleEditing={() => props.toggleEditingAt(index)}
          setName={text => props.setNameAt(text, index)}
          handleRemove={() => props.removeGuestAt(index)}
        />
    )} 
  </ul>
GuestList.PropTypes = {
  guests: PropTypes.array,
  toggleConfirmationAt: PropTypes.func,
  toggleEditingAt: PropTypes.func,
  setName: PropTypes,
  isFiltered: PropTypes.bool,
  removeGuestAt: PropTypes.func,
  pendingGuest: PropTypes.string
}

export default GuestList;