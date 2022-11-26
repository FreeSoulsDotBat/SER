import { useTheme } from "@react-navigation/native"
import { Image, StyleSheet, Text, View } from "react-native"

const viewStyle = StyleSheet.create({
	flex: 1,
	justifyContent: "center",
	height: "100%",
	width: "100%",
	alignItems: "center",
})

export const Login = () => {
	const { typography } = useTheme()
	return (
		<View style={{ ...viewStyle, backgroundColor: "white" }}>
			<View style={viewStyle}>
				<Image
					source={require("../../assets/images/logo.png")}
					style={{
						resizeMode: "contain",
						maxHeight: 250,
						maxWidth: "100%",
					}}
				/>
				<Text style={{ ...typography.lg, textTransform: "uppercase" }}>
					Escola de Reis
				</Text>
			</View>
			<View style={{ ...viewStyle, justifyContent: "flex-start" }}>
				<Text style={{ ...typography.sm, textTransform: "uppercase" }}>
					Bem-vindo
				</Text>
			</View>
		</View>
	)
}
