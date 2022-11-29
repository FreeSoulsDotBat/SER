import { useTheme } from "@react-navigation/native"
import React, { useEffect, useState } from "react"
import { Controller } from "react-hook-form"
import { StyleSheet, TextInput, Text, View } from "react-native"

export const TextInputField = ({
	control,
	rules,
	name,
	disabled,
	errors,
	label,
	placeholder,
	...rest
}) => {
	const { colors, typography } = useTheme()

	const inputBorderStyles = StyleSheet.create({
		primary: {
			borderColor: colors.darkGrey,
			borderWidth: 1,
			color: "black",
		},
		onFocus: {
			borderColor: colors.blue,
			borderWidth: 2,
			color: "black",
		},
		disabled: {
			borderColor: colors.grey,
			borderWidth: 1,
			color: colors.darkGrey,
		},
		error: {
			borderColor: colors.red,
			borderWidth: 2,
			color: colors.red,
		},
	})

	const [borderStyle, setBorderStyle] = useState(inputBorderStyles.primary)

	const onBlurHandler = fn => {
		setBorderStyle(inputBorderStyles.primary)
		return fn
	}

	useEffect(() => {
		disabled
			? setBorderStyle(inputBorderStyles.disabled)
			: setBorderStyle(inputBorderStyles.primary)

		!!errors && setBorderStyle(inputBorderStyles.error)
	}, [disabled, errors])

	return (
		<Controller
			control={control}
			rules={rules}
			render={({ field: { onChange, onBlur, value } }) => (
				<View {...rest}>
					{label && (
						<Text
							style={{
								...typography.pBolder,
								textAlign: "left",
								paddingLeft: 6,
								paddingBottom: 3,
								color: "black",
								width: "100%",
							}}>
							{label}
						</Text>
					)}
					<TextInput
						style={{
							...typography.p,
							...borderStyle,
							borderRadius: 10,
							paddingVertical: 0,
							paddingHorizontal: 10,
							width: "100%",
							height: 30,
						}}
						editable={!disabled}
						onBlur={() => onBlurHandler(onBlur)}
						onFocus={() =>
							setBorderStyle(inputBorderStyles.onFocus)
						}
						onChangeText={onChange}
						value={value}
						placeholder={placeholder}
						placeholderTextColor={colors.grey}
					/>
					{!!errors && (
						<Text
							style={{
								...typography.pBolder,
								width: "100%",
								color: colors.red,
								paddingLeft: 6,
								textAlign: "left",
							}}>
							{errors.message}
						</Text>
					)}
				</View>
			)}
			name={name}
		/>
	)
}
