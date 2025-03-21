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
import { loginFields } from '@/common/commonData';
import { customerService } from '@/api/apiUrls';
import { LoginRequest } from '@/api/types';
import { useState } from 'react';
import { Visibility, VisibilityOff } from '@mui/icons-material';
import { errorToast, successToast } from '@/common';
import Link from 'next/link';

const UserLoginForm = () => {
    const theme = useTheme();
    const {
        control,
        handleSubmit,
        formState: { errors },
    } = useForm<TScheme>({
        resolver: yupResolver(Schema),
        mode: 'onSubmit',
    });

    const [showPassword, setShowPassword] = useState(false);

    const onSubmit = async (data: TScheme) => {
        console.log("calling on submit")
        try {
            const loginData: LoginRequest = {
                username: data.username,
                password: data.password
            };

            const response = await customerService.userLogin(loginData);
            console.log('Login Successful:', response.data);
            successToast('User logged in successfully!');
        } catch (error: any) {
            console.log("error", error)
            const errorMsg = error?.response?.data?.errorMsg || 'An unexpected error occurred.';
            errorToast(errorMsg);
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
                backgroundColor: theme.mint?.color?.background?.containerBg?.layer1 || '#f5f5f5',
            }}
        >
            <form
                onSubmit={handleSubmit(onSubmit)}
                style={{
                    width: '100%',
                    maxWidth: '500px',
                    backgroundColor: '#fff',
                    padding: theme.mint?.spacing?.m || '16px',
                    borderRadius: theme.mint?.cornerRadius?.m || '8px',
                    boxShadow: '0 4px 12px rgba(0, 0, 0, 0.1)',
                }}
            >
                <Box
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        gap: theme.mint?.spacing?.m || '16px',
                    }}
                >
                    {loginFields.map((field) => (
                        <CustomInputField
                            key={field.name}
                            name={field.name}
                            label={field.label}
                            control={control}
                            errors={errors}
                            variant="outlined"
                            type={field.type}
                        />
                    ))}

                    <FormControl fullWidth variant="outlined" error={!!errors.password}>
                        <InputLabel htmlFor="password">Password</InputLabel>
                        <Controller
                            name="password"
                            control={control}
                            render={({ field }) => (
                                <OutlinedInput
                                    {...field}
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
                                />
                            )}
                        />
                        <FormHelperText>{errors.password?.message}</FormHelperText>
                    </FormControl>

                    <Button
                        variant="contained"
                        fullWidth
                        type="submit"
                        sx={{
                            background: 'linear-gradient(to right, #33E4DB, #00BBD3)',
                            color: '#fff',
                            '&:hover': {
                                background: 'linear-gradient(to right, #00BBD3, #33E4DB)',
                            },
                        }}
                    >
                        Login
                    </Button>

                    <Typography
                        variant="body2"
                        align="center"
                        sx={{ marginTop: theme.mint?.spacing?.s || '8px', color: theme.mint?.color?.background?.containerBg?.scrim || '#666' }}
                    >
                        Already have an account?{' '}
                        <Link href="/sign-in" style={{ color: theme.mint?.color?.border?.high || '#007bff' }}>
                            Sign In
                        </Link>
                    </Typography>
                </Box>
            </form>
        </Box>
    );
};

export default UserLoginForm;
