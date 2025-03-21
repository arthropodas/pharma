import { InferType, number, object, string,date,mixed } from "yup";

const phoneRegex = /^[7-9][0-9]{9}$/;

export const Schema = object().shape({
  first_name: string().required("First name is required"),
  last_name: string(),
  gender:string().required("Gender is required"),
  dob:
  string()
  .required('Date of Birth is required')
  .matches(/^\d{4}-\d{2}-\d{2}$/, 'Date of Birth must be in the format YYYY-MM-DD'),
  email: string().email('Invalid email format').required('Email is required'),
  phone_number: string()
    .matches(phoneRegex, "Give a valid phone number")
    .required("Phone number is required"),
  user_type: number(),
  password: string()
  .required('Password is required')
  .min(8, 'Password must be at least 8 characters long')
  .matches(/[a-z]/, 'Password must contain at least one lowercase letter')
  .matches(/[A-Z]/, 'Password must contain at least one uppercase letter')
  .matches(/[0-9]/, 'Password must contain at least one number')
  .matches(/[\W_]/, 'Password must contain at least one special character')
  .matches(/^\S*$/, 'Password cannot contain spaces'),

  // profile_image: mixed()
  
  // .test('is-file', 'Only PNG files are allowed', (value) => {
  //   if (!value) return true; 
  //   return value instanceof File && value.type === 'image/png'; 
  // }),

});

export type TScheme = InferType<typeof Schema>;
  
