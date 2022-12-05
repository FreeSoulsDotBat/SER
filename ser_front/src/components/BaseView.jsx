import { SafeAreaView, ScrollView, StatusBar } from "react-native"

export const BaseView = ({
	children,
	opitionalStyle,
	barColor = "dark-content",
}) => {
	return (
		<SafeAreaView style={{ flex: 1, backgroundColor: "white" }}>
			<ScrollView
				contentContainerStyle={{
					alignItems: "center",
					backgroundColor: "white",
					paddingBottom: 40,
					...opitionalStyle,
				}}
				alwaysBounceVertical>
				<StatusBar
					translucent
					backgroundColor="transparent"
					barStyle={barColor}
				/>
				{children}
			</ScrollView>
		</SafeAreaView>
	)
}
