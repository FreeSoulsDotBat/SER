import { Image, Text, View } from "react-native"

export const Opening = () => {
	return (
		<View
			style={{
				flex: 1,
				backgroundColor: "black",
				justifyContent: "center",
				alignItems: "center",
			}}>
			<View
				style={{
					flex: 2,
					justifyContent: "flex-end",
					alignItems: "center",
				}}>
				<Image
					source={require("../../assets/images/logo.png")}
					style={{
						maxHeight: 300,
						maxWidth: "70%",
					}}
				/>
			</View>
			<View
				style={{
					flex: 1,
					justifyContent: "flex-start",
					alignItems: "center",
				}}>
				<Text
					style={{
						color: "white",
						fontFamily: "Montserrat",
						fontWeight: "bold",
						fontSize: 28,
						textTransform: "uppercase",
					}}>
					Escola de Reis
				</Text>
			</View>
		</View>
	)
}
