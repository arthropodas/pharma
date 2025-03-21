import { Label } from "@mui/icons-material";

export const genderOptions = [
    { value: "1", label: "Male" },
    { value: "2", label: "Female" },
    { value: "3", label: "Other" },
  ];

  export const registerFields = [
    { name: 'first_name', label: 'First Name', type: 'text' },
    { name: 'last_name', label: 'Last Name', type: 'text' },
    // { name: 'dob', label: 'Date of Birth', type: 'date', InputLabelProps: { shrink: true } },
    { name: 'email', label: 'Email', type: 'email' },
    { name: 'phone_number', label: 'Phone Number', type: 'text' },
  ];

export const loginFields=[
  {name:"username", label:"user name", type:'string'},

]