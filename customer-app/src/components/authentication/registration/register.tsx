'use client'
import {
  Box,
  Button,
  useTheme,
  FormControl,
  InputLabel,
  FormHelperText,
  OutlinedInput,
  InputAdornment,
  IconButton,
  Typography,
} from '@mui/material';
import { yupResolver } from '@hookform/resolvers/yup';
import { Controller, useForm } from 'react-hook-form';
import { TScheme, Schema } from './Schema';
import CustomInputField from '@/common/customInput';
import CustomSelect from '@/common/customSelect';
import {genderOptions,registerFields } from '@/common/commonData';
import { customerService } from '@/api/apiUrls';
import { RegisterRequest } from '@/api/types';
import { DatePicker, DatePickerProps } from "@mui/x-date-pickers/DatePicker";
import dayjs from 'dayjs';
import { useState } from 'react';
import { Visibility, VisibilityOff } from '@mui/icons-material';
import { errorToast, successToast } from '@/common';
import Link from 'next/link';



const UserRegisterForm = () => {
  const theme = useTheme();

  const {
    control,
    handleSubmit,
    formState: { isValid, errors },
  } = useForm<TScheme>({
    resolver: yupResolver(Schema),
    mode: 'onSubmit',
  });
  const [showPassword, setShowPassword] = useState(false);

  const onSubmit = async (data: TScheme) => {
    try {
      const requestData: RegisterRequest = {
        firstName: data.first_name,
        lastName: data.last_name || '',
        gender: parseInt(data.gender),
        dob: data.dob,
        email: data.email,
        phoneNumber: data.phone_number,
        userType: 2,
        password:data.password
      };

      const response = await customerService.userRegistration(requestData);
      console.log('Registration Successful:', response.data);
      successToast('User registered successfully!');
    } catch (error: any) {
      errorToast('Registration Failed:', error?.response.data.errorMsg);
      if (error.response) {
        errorToast(error?.response.data.errorMsg);
      } else {
        errorToast('An unexpected error occurred.');
      }
    }
  };

  const handleClickShowPassword = () => setShowPassword((prev) => !prev);

  const handleMouseDownPassword = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();
  };

  
  

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        backgroundColor: theme.mint.color.background.containerBg.layer1,
      }}
    >
      <form
        onSubmit={handleSubmit(onSubmit)}
        style={{
          width: '100%',
          maxWidth: '500px',
          backgroundColor: '#fff',
          padding: theme.mint.spacing.m,
          borderRadius: theme.mint.cornerRadius.m,
          boxShadow: '0 4px 12px rgba(0, 0, 0, 0.1)',
        }}
      >
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: theme.mint.spacing.m,
          }}
        >
       
          {registerFields.map((registerFields) => (
            <CustomInputField
              key={registerFields?.name}
              name={registerFields?.name}
              label={registerFields?.label}
              control={control}
              errors={errors}
              variant="outlined"
              type={registerFields.type}
              // {...(registerFields.InputLabelProps ? { InputLabelProps: registerFields.InputLabelProps } : {})}
            />
          ))}

         
          <FormControl fullWidth error={!!errors.gender}>
                      <CustomSelect
              name="gender"
              label="Gender"
              options={genderOptions}
              control={control}
              error={errors.gender}
            />
           
     
          </FormControl>

          <FormControl fullWidth error={!!errors.dob}>
          
          <Controller
  name="dob"
  control={control}
  render={({ field }: any) => (
    <DatePicker
      {...field}
      label="Date of Birth"
      format="YYYY-MM-DD"
      value={field.value ? dayjs(field.value) : null}
      error={!!errors.dob} // Make sure error is passed to the input field
      helperText={errors.dob ? errors.dob.message : ''}
      onChange={(value) => {
        if (value) {
          field.onChange(dayjs(value).format('YYYY-MM-DD'));
        } else {
          field.onChange(''); // Handle null value
        }
      }}
      slotProps={{
        textField: {
          error: !!errors.dob,
          helperText: errors.dob ? errors.dob.message : '',
          fullWidth: true, // You can add additional props for the text field here
        },
      }}
    />
  )}
/>

            
          </FormControl>

          <FormControl fullWidth variant="outlined" error={!!errors.password}>
            <InputLabel htmlFor="password">Password</InputLabel>
            <OutlinedInput
              id="password"
              type={showPassword ? 'text' : 'password'}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                    edge="end"
                  >
                    {showPassword ? <Visibility /> : <VisibilityOff />}
                  </IconButton>
                </InputAdornment>
              }
              label="Password"
              autoComplete="new-password"

              {...control.register('password')}
            />
            <FormHelperText>{errors.password ? errors.password.message : ''}</FormHelperText>
          </FormControl>

          <Button
  variant="contained"
  fullWidth
  type="submit"
  // disabled={!isValid}
  sx={{
    background:'linear-gradient(to right, #33E4DB, #00BBD3)',
    color: '#fff', 
    '&:hover': {
      background: 'linear-gradient(to right, #00BBD3, #33E4DB)', 
    },
  }}
>
  Register
</Button>
<Typography
            variant="body2"
            align="center"
            sx={{ marginTop: theme.mint.spacing.s ,color: theme.mint.color.background.containerBg.scrim}}
          >
            Already have an account?{' '}
            <Link href="/sign-in" style={{ color: theme.mint.color.border.high }}>
              Sign In
            </Link>
          </Typography>

          
        </Box>
      </form>
    </Box>
  );
};

export default UserRegisterForm;
