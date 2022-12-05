import { useTheme } from "@react-navigation/native"
import React, { useEffect, useState } from "react"
import { StyleSheet, Pressable, Text } from "react-native"

export const ButtonComponent = ({
	title,
	variant,
	size,
	optionalStyles,
	...rest
}) => {
	const { colors, typography } = useTheme()

	const buttonTemplateStyles = StyleSheet.create({
		primary: {
			backgroundColor: colors.beige,
			borderRadius: 40,
			lineHeight: 0,
			justifyContent: "center",
			alignItems: "center",
		},
		secondary: {
			backgroundColor: colors.blue,
			borderRadius: 40,
			lineHeight: 0,
			justifyContent: "center",
			alignItems: "center",
		},
		loading: {},
	})

	const buttonSizes = StyleSheet.create({
		full: {
			width: "100%",
			height: 40,
		},
		xl: {
			width: 200,
			height: 35,
		},
		lg: {
			width: 160,
			height: 30,
		},
		md: {
			width: 120,
			height: 30,
		},
		sm: {
			width: 100,
			height: 30,
		},
	})

	const fontSizes = StyleSheet.create({
		full: typography.md,
		xl: typography.md,
		lg: typography.pBolder,
		md: typography.pBolder,
		sm: typography.pBolder,
	})

	const buttonSize = buttonSizes[size]
	const fontSize = fontSizes[size]
	const templateStyle = buttonTemplateStyles[variant]

	return (
		<Pressable
			style={{
				...buttonSize,
				...templateStyle,
				...optionalStyles,
			}}
			{...rest}>
			<Text style={{ ...fontSize, color: "white" }}>{title}</Text>
		</Pressable>
	)
}
